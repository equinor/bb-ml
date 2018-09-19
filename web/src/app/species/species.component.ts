import { Component, OnInit, Input } from '@angular/core';
import { DataService } from '../_services/data.service';
import { Well } from '../_model/types';

@Component({
  selector: 'app-species',
  templateUrl: './species.component.html',
  styleUrls: ['./species.component.css']
})
export class SpeciesComponent implements OnInit {
  speciesList: any;
  objectKeys = Object.keys;
  wells: Well[];

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.speciesList = this.dataService.species;
    this.wells = this.dataService.wells;
  }
}
