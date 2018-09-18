import { Component, OnInit } from '@angular/core';
import { DataService } from '../_services/data.service';
import { Sample, Well } from '../_model/types';

@Component({
  selector: 'app-well',
  templateUrl: './well.component.html',
  styleUrls: ['./well.component.css']
})
export class WellComponent implements OnInit {
  selectedWell: Well;
  wells: Well[];
  selectedSample: Sample;

  constructor(private dataService: DataService) {}

  ngOnInit() {
    this.dataService.getWells().subscribe(data => {
      this.wells = data;
    });
  }

  wellChanged(event: any): void {
    this.selectedSample = null;
  }

  setSample(sample: Sample): void {
    this.selectedSample = sample;
  }
}
