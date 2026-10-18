# Integration review — October 17, 2026

| Source | Implementation / limit |
|---|---|
|https://openrxdata.com/about|Design inspiration; published inputs include FDA labels/NDC, RxNorm and CMS pricing/coverage. Not an exhaustive dependency audit.|
|https://www.hiv-druginteractions.org/terms|Limited linking permitted; content reuse requires permission. HIV, PrEP, HEP and COVID checkers open separately. No interaction database imported.|
|https://learningaboutdiabetes.org/programs-consumer/|English/Spanish consumer directory. Sample insulin-pen PDF restricts healthcare-professional use; no copied handouts or blanket reading-grade claim.|
|https://app.pyrls.com/home|Uploaded recording sampled across five frames; category/card layout inspiration only, no copied proprietary charts.|
|https://open.fda.gov/apis/drug/drugshortages/how-to-use-the-endpoint/|New API adapter with generic_name/proprietary_name queries. No result is not evidence of availability. Browser CORS acceptance pending.|
|https://www.medicaid.gov/medicaid/nadac|Candidate weekly acquisition-cost integration. Exact NDC, unit and effective date needed; not patient cash price/copay.|
|https://clinicaltrials.gov/data-api|Candidate trial-registry integration; registration does not establish efficacy.|

Public availability is not an open-source license. Existing RxNorm/RxTerms, label, MedlinePlus and PubMed integrations remain. New sources enter a review queue; no source content automatically changes clinical recommendations.
