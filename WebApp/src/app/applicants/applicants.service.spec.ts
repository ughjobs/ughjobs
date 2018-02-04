import { TestBed, inject } from '@angular/core/testing';

import { ApplicantsService } from './applicants.service';

describe('ApplicantsService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ApplicantsService]
    });
  });

  it('should be created', inject([ApplicantsService], (service: ApplicantsService) => {
    expect(service).toBeTruthy();
  }));
});
