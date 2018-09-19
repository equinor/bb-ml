import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { MyMaterialModule } from './amaterial-module';
import { HttpClientModule } from '@angular/common/http';
import { SpeciesComponent } from './species/species.component';
import { WellComponent } from './wells/well.component';
import { DataService } from './_services/data.service';
import { SpeciesChartComponent } from './species-chart/species-chart.component';
import { OrderModule } from 'ngx-order-pipe';
import { NgxChartsModule } from '@swimlane/ngx-charts';

const appRoutes: Routes = [
  { path: '', component: WellComponent, pathMatch: 'full'},
  { path: 'rawdata', component: WellComponent },
  { path: 'allspecies', component: SpeciesComponent }
];

@NgModule({
  declarations: [AppComponent, WellComponent, SpeciesComponent, SpeciesChartComponent],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    RouterModule.forRoot(appRoutes),
    HttpClientModule,
    MyMaterialModule,
    OrderModule,
    NgxChartsModule
  ],
  providers: [DataService],
  bootstrap: [AppComponent]
})
export class AppModule {}
