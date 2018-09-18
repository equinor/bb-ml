import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { MyMaterialModule } from './amaterial-module';
import { HttpClientModule } from '@angular/common/http';
import { SpeciesComponent } from './species/species.component';
import { WellComponent } from './wells/well.component';

const appRoutes: Routes = [
  { path: 'rawdata', component: WellComponent }
  // { path: 'other', component: Other }
];

@NgModule({
  declarations: [AppComponent, WellComponent, SpeciesComponent],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    RouterModule.forRoot(appRoutes),
    HttpClientModule,
    MyMaterialModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
