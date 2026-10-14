(function(root){'use strict';
const definitions=[
['Indications',['indications_and_usage','purpose'],[]],
['Mechanism of action',['mechanism_of_action'],['clinical_pharmacology']],
['Dosage and administration (combined; verify adult/pediatric applicability)',['dosage_and_administration'],[]],
['Strengths',['dosage_forms_and_strengths'],['how_supplied']],
['Boxed warning',['boxed_warning'],[]],['Contraindications',['contraindications'],[]],
['Warnings',['warnings_and_cautions','warnings'],[]],
['Adverse reactions (severity not classified by this tool)',['adverse_reactions'],[]],
['Interactions',['drug_interactions'],[]],
['Pediatric use',['pediatric_use'],['use_in_specific_populations']],
['Pregnancy',['pregnancy'],['use_in_specific_populations']],
['Lactation',['nursing_mothers','lactation'],['use_in_specific_populations']],
['Renal/hepatic considerations',[],['use_in_specific_populations']],
['Pharmacokinetics',['pharmacokinetics'],['clinical_pharmacology']],
['Patient counseling',['patient_counseling_information','patient_medication_information','patient_medguide'],[]],
['Storage',['storage_and_handling'],[]]];
function normalize(label){const text=k=>Array.isArray(label[k])?label[k].filter(x=>typeof x==='string').join(' ').replace(/<[^>]*>/g,' ').trim():'';
return definitions.map(([title,direct,broad])=>{const key=direct.find(k=>text(k))||broad.find(k=>text(k));const status=!key?'NOT_RETURNED':direct.includes(key)?'FIELD_RETURNED':'BROADER_SECTION_REVIEW';return {title,status,field:key||null,text:status==='FIELD_RETURNED'?text(key):status==='BROADER_SECTION_REVIEW'?'Review the broader '+key+' section in the exact source label; no topic-specific finding is inferred.':'Not returned by this API record. This does not mean absent risk or no applicable guidance.'};});}
const api={normalize};if(typeof module==='object'&&module.exports)module.exports=api;else root.ClinicalMedicationSections=api;
})(typeof window!=='undefined'?window:globalThis);
