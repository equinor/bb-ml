import { Component, OnInit, Input } from '@angular/core';
import { Sample } from '../wells/well.component';

@Component({
  selector: 'app-species',
  templateUrl: './species.component.html',
  styleUrls: ['./species.component.css']
})
export class SpeciesComponent implements OnInit {
  @Input() selectedSample: Sample;
  constructor() { }

  ngOnInit() {
  }

}

export class Species {
  SpeciesName: string;
  Code: string;
  SpeciesId: number;
  SpeciesCount?: number;
  Abundance?: string;
}
