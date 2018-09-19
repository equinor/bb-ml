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
  MatGridListModule,
  MatTableModule
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
    MatGridListModule,
    MatTableModule
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
    MatGridListModule,
    MatTableModule
  ]
})
export class MyMaterialModule {}
