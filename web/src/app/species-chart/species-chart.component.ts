import { Component, OnInit, Input } from '@angular/core';
import { Sample } from '../_model/types';

@Component({
  selector: 'app-species-chart',
  templateUrl: './species-chart.component.html',
  styleUrls: ['./species-chart.component.css']
})
export class SpeciesChartComponent implements OnInit {
  @Input() sample: Sample;
  constructor() { }

  ngOnInit() {
  }

}
