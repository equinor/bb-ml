import { Well } from './wells/well.component';

export const DUMMY_WELLS: Well[] = [
  {
    WellName: 'N15/9-F-1A',
    WellCode: 'N1509F01A',
    Operator: 'Statoil',
    Field: 'Volve',
    Country: 'NOCS',
    Type: 'Borehole',
    Units: 'metres',
    Longitude: 0.0,
    Latitude: 0.0,
    TerminalDepth: 6000.0,
    DepthDatum: 'RTE',
    Samples: [
      {
        BaseDepth: 3358,
        Type: 'CU',
        Created: '05-Dec-2013',
        Modified: '05-Dec-2013',
        SampleId: 1,
        Label: 'L527',
        Species: [
          {
            SpeciesName: 'Algal cells (ribbed)',
            SpeciesId: 13862,
            Code: 'AL',
            SpeciesCount: 2
          },
          {
            SpeciesName: 'Algal cells (thalloid - fibrous)',
            SpeciesId: 13925,
            Code: 'AL',
            SpeciesCount: 2
          },
          {
            SpeciesName: 'Algal cells (thalloid - Type 1)',
            SpeciesId: 13829,
            Code: 'AL',
            SpeciesCount: 3
          },
          {
            SpeciesName: 'Apteodinium daveyi',
            SpeciesId: 10943,
            Code: 'DC',
            SpeciesCount: 2
          },
          {
            SpeciesName: 'Achomosphaera ramulifera Evitt,W.R., 1963',
            SpeciesId: 7306,
            Code: 'DC',
            SpeciesCount: 2
          },
          {
            SpeciesName: 'Achomosphaera spp.',
            SpeciesId: 8854,
            Code: 'DC',
            SpeciesCount: 3
          },
          {
            SpeciesName: 'Apteodinium grande',
            SpeciesId: 4196,
            Code: 'DC',
            SpeciesCount: 6
          },
          {
            SpeciesName: 'Bisaccates undiff.',
            SpeciesId: 9118,
            Code: 'PO',
            SpeciesCount: 8
          }
        ]
      },
      {
        BaseDepth: 3364,
        Type: 'CU',
        Created: '05-Dec-2013',
        Modified: '05-Dec-2013',
        SampleId: 3,
        Label: 'L528',
        Species: [
          {
            SpeciesName: 'Achomosphaera ramulifera Evitt,W.R., 1963',
            SpeciesId: 7306,
            Code: 'DC',
            SpeciesCount: 2
          },
          {
            SpeciesName: 'Achomosphaera spp.',
            SpeciesId: 8854,
            Code: 'DC',
            SpeciesCount: 3
          },
          {
            SpeciesName: 'Apteodinium grande',
            SpeciesId: 4196,
            Code: 'DC',
            SpeciesCount: 6
          },
          {
            SpeciesName: 'Bisaccates undiff.',
            SpeciesId: 9118,
            Code: 'PO',
            SpeciesCount: 8
          }
        ]
      }
    ]
  },
  {
    WellName: 'N15/9-F-1B',
    WellCode: 'N1509F01B',
    Operator: 'Statoil',
    Field: 'Volve',
    Country: 'NOCS',
    Type: 'Borehole',
    Units: 'metres',
    TerminalDepth: 6000.0,
    DepthDatum: 'RTE',
    Samples: [
      {
        BaseDepth: 3160,
        Type: 'CU',
        Created: '15-Dec-2013',
        Modified: '15-Dec-2013',
        SampleId: 1,
        Label: 'M94',
        Species: [
          {
            SpeciesName: 'Achomosphaera ramulifera Evitt,W.R., 1963',
            SpeciesId: 7306,
            Code: 'DC',
            SpeciesCount: 2
          },
          {
            SpeciesName: 'Achomosphaera spp.',
            SpeciesId: 8854,
            Code: 'DC',
            SpeciesCount: 3
          },
          {
            SpeciesName: 'Apteodinium grande',
            SpeciesId: 4196,
            Code: 'DC',
            SpeciesCount: 6
          },
          {
            SpeciesName: 'Bisaccates undiff.',
            SpeciesId: 9118,
            Code: 'PO',
            SpeciesCount: 8
          }
        ]
      }
    ]
  }
];
