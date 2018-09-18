import { Component, OnInit, Input } from '@angular/core';
import { DataService } from '../_services/data.service';

@Component({
  selector: 'app-species',
  templateUrl: './species.component.html',
  styleUrls: ['./species.component.css']
})
export class SpeciesComponent implements OnInit {
  speciesList: any;
  objectKeys = Object.keys;

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.speciesList = this.dataService.species;
  }

}
