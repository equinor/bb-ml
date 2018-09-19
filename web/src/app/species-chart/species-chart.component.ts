import {
  Component,
  OnInit,
  Input,
  AfterViewInit,
  OnChanges
} from '@angular/core';
import { Sample } from '../_model/types';

@Component({
  selector: 'app-species-chart',
  templateUrl: './species-chart.component.html',
  styleUrls: ['./species-chart.component.css']
})
export class SpeciesChartComponent implements OnInit, OnChanges {
  @Input()
  sample: Sample;
  chartData: any[];
  showXAxis = true;
  showYAxis = true;
  gradient = false;
  showLegend = false;
  showXAxisLabel = false;
  xAxisLabel = 'xaxis';
  showYAxisLabel = false;
  yAxisLabel = 'yaxis';
  view: any[] = [700, 650];
  ticks: any[] = [];
  colorScheme = {
    domain: ['#5AA454', '#A10A28', '#C7B42C', '#AAAAAA']
  };

  constructor() {}

  ngOnInit() {
    // this.chartData = [];
    // this.sample.Species.forEach(spec => {
    //   this.chartData.push({ name: spec.SpeciesName, value: spec.SpeciesCount });
    // });
    // console.log(this.chartData);
  }
  ngOnChanges(): void {
    this.chartData = [];
    this.sample.Species.forEach(spec => {
      this.chartData.push({ name: spec.SpeciesName, value: spec.SpeciesCount });
    });
    console.log(this.chartData);
  }

  formatPercent(val) {
    if (val <= 100) {
      return val + '%';
    }
  }
  onSelect(event) {
    console.log(event);
  }
}
