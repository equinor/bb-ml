import { Component, OnInit } from '@angular/core';
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

  constructor(private dataService: DataService) {}

  ngOnInit() {
    this.dataService.getWells().subscribe(data => {
      this.wells = data;
    });
  }

  wellChanged(event: MatSelectChange): void {
    this.selectedSample = null;
    this.dataService.getSamples(event.value.WellName).subscribe(data => {
      this.samples = data.Depth;
    });
  }

  setSample(sample: Sample): void {
    this.selectedSample = sample;
  }
}
