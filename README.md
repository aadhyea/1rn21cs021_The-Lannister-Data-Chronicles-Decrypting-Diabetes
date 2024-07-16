# S.U.I.T.S Hackathon

## PROBLEM STATEMENT CHOSEN -
The Lannister Data Chronicles: Decrypting Diabetes

In the opulent halls of Casterly Rock, where riches abound and power is wielded with a cunning hand, a new shadow looms over House Lannister: diabetes, a silent adversary threatening even the mightiest of lineages. From Lord Tywin to Lady Cersei, no one is immune to its grasp, and the need for answers becomes paramount.

The maesters of the Citadel, renowned for their wisdom and knowledge, have assembled a vast trove of data as intricate as the schemes spun in the Red Keep. This dataset, composed solely of numerical attributes, holds the secrets to understanding why some Lannisters succumb to this unseen foe while others defy its clutches.

At the heart of this quest stands Lord Agasthyrion, a revered sage of data from a distant northern keep, known for his unyielding intellect and mastery of statistical analysis and machine learning. With steely resolve, he delves into the depths of the dataset, uncovering buried truths and weaving together threads of information that hint at the true drivers of diabetes within House Lannister.

## PROBLEM STATEMENT CHUNKS

- Chunk 1
  - One crucial attribute becomes the focus of Agasthyrion's analysis. For each data point, a value of 0 signifies no diabetes, 1 indicates prediabetes, and 2 marks the onset of diabetes. Agasthyrion ponders over these classifications, seeking to understand the implications of a value of 0 and what it truly represents within the broader context of health behaviors.

  - Time is fleeting, and every day brings new challenges. Lives hang in the balance as Agasthyrion's quest becomes a race against time to uncover the secrets that could determine the fate of House Lannister. His mission is not merely scholarly; it is a crusade to safeguard the future health of his noble kin. With each discovery, Agasthyrion calls upon the maesters to make bold predictions based on their findings. Like predicting the outcome of battles or the allegiance of houses, these predictions could sway the course of health within House Lannister. The stakes are high, and Agasthyrion's leadership becomes paramount as he guides his allies through the intricate dance of data science.

- Chunk 2

  - But Agasthyrion's path is fraught with peril. As whispers of his discoveries echo through the gilded corridors of Casterly Rock, rival factions within the family vie for control of the knowledge hidden within the data. Yet, driven by his quest for understanding and fueled by a desire to protect the honor of House Lannister, Agasthyrion presses onward. In his quest, Agasthyrion seeks to identify hidden patterns and groupings within the data, revealing health behavior profiles that might explain why certain individuals fall prey to diabetes while others remain unscathed. This analysis, intricate and complex, could unveil the unseen dynamics that influence the health of House Lannister.

  - As winter's chill descends upon Casterly Rock, Agasthyrion summons the brightest minds of the house to join him in the battle against diabetes. From the sunlit chambers of Lannisport to the shadowy corners of the Westerlands, he seeks allies who will wield their knowledge like Valyrian steel, crafting reports that dissect the mysteries concealed within the data.

- Chunk 3
  - As ravens carry his summons across the lands, Agasthyrion waits with bated breath for insights that will shape the future of health within House Lannister. As the game of data unfolds, the fate of House Lannister's health hangs in the balance, and Agasthyrion stands as their stalwart defender against the encroaching darkness. The maesters gather, parchments filled with secrets and revelations, eager to unveil the enigmatic forces that decide the destiny of each Lannister. In the midst of their deliberations, one maester suggests invoking the wisdom hidden within the patterns of the data, while another proposes a methodical approach to reveal the truths buried deep. They cast these powerful analyses, revealing hidden pathways to health or peril. With graphs and charts depicting the nuances of each type of diabetes, they prepare to present their findings to Agasthyrion, guiding House Lannister towards a future where health and prosperity reign supreme.

## SOLUTION APPROACH

The provided dataset is raw. So, EDA has been performed and using various plots the data is also visualised for better understanding. Then, we can either use a Random Forest or Gradient Boosting Classifier model to predict if the person has diabetes or not. In the solution we have used Random Forest and the accuracy of the prediction is about 85%.


To visualize the dashboard, simply run the file `DASHBOARD.py` or type the command `python -u DASHBOARD.py`
