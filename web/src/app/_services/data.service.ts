import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Well } from '../_model/types';

@Injectable()
export class DataService {
  species: any;

  constructor(private http: HttpClient) {
    this.getSpecies().subscribe(data => {
      this.species = data;
    });
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
}
