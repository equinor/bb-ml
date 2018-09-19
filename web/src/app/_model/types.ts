export class Species {
  SpeciesName: string;
  Code: string;
  SpeciesId: string;
  SpeciesCount?: number;
  Abundance?: string;
}

export class Well {
  WellName: string;
  WellCode: string;
  Operator: string;
  Field: string;
  Country: string;
  Type: string;
  Units: string;
  Longitude?: number;
  Latitude?: number;
  TerminalDepth: number;
  DepthDatum: string;
  Samples: Sample[];
}

export class Sample {
  BaseDepth: number;
  Type: string;
  Created: string;
  Modified: string;
  SampleId: number;
  Label: string;
  Id: string;
  Species: Species[];
}
