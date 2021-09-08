## Logistic Regression Problem - Classify Ad Clicking activity by a Facebook User


#### Problem Description:
- Analyse the click activity data where each row represents a user activity on Facebook.
- A user either clicks on the appearing ad or not, this could be inferred based on his/her activity and the objective is to predict the action on a newly appearing ad performed by the user.

#### Data description:
| _Column Name_| _Description_ | _Observation_ | _Action_ | 
| -           | -           | -           | - |
| Names | Name of the user | Unique or Highly cardinal column| Can be dropped | 
| emails | Email id of the user | Unique or Highly cardinal column| Can be dropped |
| Country | Country the user session is appearing from | Highly cardinal column| Can be replaced with Continent |
| Time Spent on Site | Minutes spent by user during session | | |
| Salary | Salary of user | | |
| Clicked | 1 if user clicked on the ad <br> 0 if user didnt click on the ad <br> **Target Variable** | | Binary Classifier can be applied|



