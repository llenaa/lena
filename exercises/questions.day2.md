# Questions on the article 'The Progenetix oncogenomic resource in 2021'

- What is CNV/CNA?
  - CNA = Copy number aberrations
  - CNV = Copy number variation


- How will you describe or introduce progenetix (scale, data source, cancer types and
so on)?

  The Progenetix database provides an overview of mutation data in cancer, with a focus on copy number abnormalities (CNV / CNA), for all types of human malignancies. The data is based on individual sample data from currently 142063 samples. It includes data of 834 different cancer tpes, mapped to a variety of technical and medical categories.
  A possible use of the databank can be the search for local copy number aberrations, involving for example a gene, and the exploration of cancer types with these CNVs. The Search Page provides example use cases for designing queries. The results contain statistics but also visualization and download options[^1].
  [^1]: [https://progenetix.org/]

- Describe NCIt, ICOD, UBERON codes, and their relationships.

  NCIt is the National Cancer Institute Thesaurus. ICDO means International Classification of Diseases in Oncology. It is
limited to hierachical concepts and is hard to apply to modern ontologies. NCIt was developed more dynamical and
therefore layering data aggregations and transferring to other systems and resources is possible. Connecting the two
was done to make use of the hierarchical benefits ICDO has.
UBERON allows cross-species anatomical structural ontology. In a resource update, ICDO T codes were mapped to UBERON terms.


- What are CNV segmentations and CNV frequencies, and how to use them?

  <img width="366" alt="Screen Shot 2022-09-21 at 14 34 48" src="https://user-images.githubusercontent.com/113988381/191505328-81fdfe02-9378-49f1-b8bc-dabdc7eadad5.png">
  
  CNV frequencies are higher if the CNV is older and heritable. On the image the cancer type classification are sorted by the frequency of matching smaples in the used subset. Estimating the frequency distribution of CNVs is useful to characterize new types of genetic variation [^2].
[^2]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2562008/

- What are APIs and how to use APIs in progenetix?

  API means application programming interface. Making use of API allowed extending features of the resources and
open data to be the standard.


- How does progenetix visualise CNA profiles?

  The visualization can be customized via visulization options. For example, one could watch put for selected chromosomal regions or group the data 
  by subset and studies. Alternatively, users can also upload their own data for single or multiple sam- ples to visualize genome-wide CNA.
                               
- What do you think should be improved in progenetix?
  
  The project overall could be communicated in a more accessible manner for the public since it serves everyone and is open source. Adding a small section that is inviting and understadable would be nice. The geographic distribution, as seen on the image below (Geographic distribution by corresponding author of the genomic array, chromosmal CGH and whole genome/exome based cancer genome datasets from the 3373 listed publications) , of the authors also shows that many countries and continents are underrepresented. In my understanding some CNVs are probably not distributed too evenly and therefore it would be important to include data from everywhere in order to serve people equally and take care of everyones health with the same efforts.
  
<img width="628" alt="Screen Shot 2022-09-21 at 15 16 52" src="https://user-images.githubusercontent.com/113988381/191513980-b7ab975d-23ca-4fce-b2d9-6858d88c2ee2.png">

  

