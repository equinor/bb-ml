import { Component, OnInit, AfterViewInit } from '@angular/core';
import { DataService } from '../_services/data.service';
import { Sample, Well } from '../_model/types';
import { MatSelectChange } from '@angular/material';

@Component({
  selector: 'app-well',
  templateUrl: './well.component.html',
  styleUrls: ['./well.component.css']
})
export class WellComponent implements OnInit {
  objectKeys = Object.keys;
  selectedWell: Well;
  wells: Well[];
  selectedSample: Sample;
  samples: Object[];
  classification: any;

  constructor(private dataService: DataService) {}

  ngOnInit() {
    this.dataService.getFormattedWellData().subscribe(data => {
      this.wells = data;
    });
  }

  wellChanged(event: MatSelectChange): void {
    this.selectedSample = null;
  }

  setSample(sample: Sample): void {
    this.selectedSample = sample;
    this.classification = null;
    this.getClassification(sample);
  }

  getClassification(sample: Sample): void {
    let fossils = '{';
    sample.Species.forEach(species => {
      fossils = fossils + '"' + species.SpeciesId + '": ' + species.SpeciesCount + ',';
    });
    fossils = fossils.slice(0, -1);
    fossils = fossils + '}';
    console.log(fossils);
    this.dataService.getClassification(fossils, classification => {
      this.classification = classification;
    });
  }
}
