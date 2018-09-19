import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Well, Sample, Species } from '../_model/types';

@Injectable()
export class DataService {
  species: any;
  wells: Well[];
  private labels: any;

  constructor(private http: HttpClient) {
    this.getSpecies().subscribe(data => {
      this.species = data;
    });
    this.formatWellData();
  }

  getWells(): Observable<any> {
    return this.http.get('./assets/wells.json');
  }

  getSpecies(): Observable<any> {
    return this.http.get('./assets/species_dict.json');
  }

  getLabels(wellName: string): Observable<any> {
    return this.http.get('./assets/' + wellName + '/labels.json');
  }

  getSamples(wellName: string): Observable<any> {
    return this.http.get('./assets/' + wellName + '/samples.json');
  }

  getSpeciesSampleData(wellName: string): Observable<any> {
    return this.http.get(
      './assets/' + wellName + '/species_count_per_sample.json'
    );
  }

  getClassification(fossilAssemblage: any, callback: Function): void {
    this.http
      .post('http://localhost:5002/api/post_classification', fossilAssemblage)
      .subscribe(Response => {
        if (callback != null) {
          callback(Response);
        }
      });
  }

  getFormattedWellData(): Observable<any> {
    return this.http.get('./assets/formattedrawdata.json');
  }

  formatWellData(): void {
    this.getWells().subscribe((data: Well[]) => {
      this.wells = data;
      // console.log(this.wells[0]);
      this.wells.forEach(well => {
        well.Samples = [];
        // console.log(well.WellName);
        this.getLabels(well.WellName).subscribe(lbls => {
          this.labels = lbls.label;
        });
        this.getSamples(well.WellName).subscribe((smpls: any) => {
          Object.keys(smpls.Depth).forEach(key => {
            const sampleToPush = new Sample();
            sampleToPush.Id = key;
            sampleToPush.BaseDepth = smpls.Depth[key];
            sampleToPush.Label = this.labels[key];
            sampleToPush.Species = [];
            this.getSpeciesSampleData(well.WellName).subscribe(sps => {
              Object.keys(sps).forEach(key1 => {
                const speciesToPush = new Species();
                speciesToPush.SpeciesId = key1;
                speciesToPush.SpeciesName = this.species[key1];
                speciesToPush.SpeciesCount = sps[key1][sampleToPush.Id];
                sampleToPush.Species.push(speciesToPush);
              });
            });
            sampleToPush.Species.sort(sp => +sp.SpeciesId);
            well.Samples.push(sampleToPush);
            well.Samples.sort(s => s.BaseDepth);
          });
        });
      });
      console.log(this.wells);
    });
  }
}
