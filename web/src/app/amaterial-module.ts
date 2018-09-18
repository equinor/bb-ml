import { NgModule } from '@angular/core';
import {
  MatButtonModule,
  MatToolbarModule,
  MatSelectModule,
  MatCardModule,
  MatOptionModule,
  MatFormFieldModule,
  MatListModule,
  MatExpansionModule,
  MatGridListModule
} from '@angular/material';

@NgModule({
  imports: [
    MatButtonModule,
    MatToolbarModule,
    MatSelectModule,
    MatCardModule,
    MatOptionModule,
    MatFormFieldModule,
    MatListModule,
    MatExpansionModule,
    MatGridListModule
  ],
  exports: [
    MatButtonModule,
    MatToolbarModule,
    MatSelectModule,
    MatCardModule,
    MatOptionModule,
    MatFormFieldModule,
    MatListModule,
    MatExpansionModule,
    MatGridListModule
  ]
})
export class MyMaterialModule {}
