import { Component, OnInit } from '@angular/core';
import { DUMMY_WELLS } from '../dummy.data';
import { Species } from '../species/species.component';

@Component({
  selector: 'app-well',
  templateUrl: './well.component.html',
  styleUrls: ['./well.component.css']
})
export class WellComponent implements OnInit {
  selectedWell: Well;
  wells: Well[];
  selectedSample: Sample;
  constructor() {}

  ngOnInit() {
    this.wells = DUMMY_WELLS;
  }

  wellChanged(event: any): void {
    this.selectedSample = null;
  }
}

export class Well {
  WellName: string;
  WellCode: string;
  Operator: string;
  Field: string;
  Country: string;
  Type: string;
  Units: string;
  Longitude?: number;
  Latitude?: number;
  TerminalDepth: number;
  DepthDatum: string;
  Samples: Sample[];
}

export class Sample {
  BaseDepth: number;
  Type: string;
  Created: string;
  Modified: string;
  SampleId: number;
  Label: string;
  Species: Species[];
}
