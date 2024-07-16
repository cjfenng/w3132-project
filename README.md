# w3132-project
# COMS W3132 Individual Project

## Author
*Your name and email goes here.*
JinFeng Chen
jc6040@columbia.edu

## Project Title
*Provide a short and descriptive title for your project.*
Quantitative Trading Platform

## Project Description
*Write a short, concise project description of what your project aims to achieve. Include the motivation for this project (why do you want to work on it), the problem your project aims to solve, and the main goals that you want to accomplish within the rest of the semester. Also mention why you think the project might be useful or interesting to others. Keep this section short. A couple of paragraphs would do.*

1.Data Collection: Gather stock data.
2.Model Training: Use the collected data to train models.
3.Price Prediction: Use regression models to predict future stock prices.
4.Strategy Development: Develop strategies based on the models.
5.Backtesting: Backtest and evaluate the strategies.

## Timeline

*To track progress on the project, we will use the following intermediate milestones for your overall project. Each milestone will be marked with a tag in the git repository, and we will check progress and provide feedback at key milestones.*

| Date               | Milestone                                                                                              | Deliverables                        | Git tag    |
|--------------------|--------------------------------------------------------------------------------------------------------|-------------------------------------|------------|
| **July&nbsp;15**   | Submit project description                                                                             | README.md                           | proposal   |
| **July&nbsp;17**   | Update project scope/direction based on instructor/TA feedback                                         | README.md                           | approved   |
| **July&nbsp;22**   | Basic project structure with empty functions/classes (incomplete implementation), architecture diagram | Source code, comments, docs         | milestone1 |
| **August&nbsp;2**  | More or less complete implementation. The goal is to have something you can share with others.         | Source code, unit tests             | milestone2 |
| **August&nbsp;9**  | Complete implementation. Final touches (conclusion, documentation, testing, etc.)                      | Source code, Conclusion (README.md) | conclusion |

*The column Deliverables lists deliverable suggestions, but you can choose your own, depending on the type of your project.*

## Requirements, Features and User Stories
*List the key requirements or features of your project. For each feature, provide a user story or a simple scenario explaining how the feature will be used. You don't have to get this section right the first time. Your understanding of the problem and requirements will improve as you work on your project. It is okay (and desirable) to come back to this section and revise it as you learn more about the problem you are trying to solve. The first version of this section should reflect your understanding of your problem at the beginning of the project.*

Data Collection: Ability to collect and store historical stock data.
Model Training: Use historical data to train regression models.
Price Prediction: Predict future stock prices using trained models.
Strategy Development: Create trading strategies based on model predictions.
Backtesting: Evaluate strategies using historical data.

*Also list any required hardware, software, on online services you will need. In specific cases, we might be able to lend you hardware or obtain online services. Please email the instructor for more details.*
Hardware: Standard computer or laptop
Software: Python 
Online Services: GitHub, financial data APIs 

## Technical Specification
*Detail the main algorithms, libraries, and technologies you plan to use. Explain your choice of technology and how it supports your project goals.*
Algorithms: Linear Regression, Time Series Analysis
Pandas: For data manipulation and analysis
NumPy: For numerical computations
scikit-learn: For model training and evaluation
Matplotlib/Seaborn: For data visualization

## System or Software Architecture Diagram
*Include a block-based diagram illustrating the architecture of your software or system. This should include major components, such as user interface elements, back-end services, and data storage, and show how they interact. Tools like Lucidchart, Draw.io, or even hand-drawn diagrams photographed and uploaded are acceptable. The purpose of the diagram is to help us understand the architecture of your solution. Diagram asthetics do not matter and will not be graded.*
       +-----------------------+
       | User Interface (CLI)  |
       +----------+------------+
                  |
                  v
       +----------+------------+
       |    Data Collection    |
       +----------+------------+
                  |
                  v
       +----------+------------+
       |     Data Storage      |
       +----------+------------+
                  |
                  v
       +----------+------------+
       |    Model Training     |
       +----------+------------+
                  |
                  v
       +----------+------------+
       |  Price Prediction     |
       +----------+------------+
                  |
                  v
       +----------+------------+
       | Strategy Development  |
       +----------+------------+
                  |
                  v
       +----------+------------+
       |    Backtesting        |
       +-----------------------+

## Development Methodology
*Describe the methodology you'll use to organize and progress your work.*

*First, describe your plan for developing your project. This might include how (or if) you plan to use*
- *GitHub projects board to track progress on tasks and milestones*
- *GitHub issues to keep track of issues or problems*
- *Separate Git branches and/or GitHub pull requests for development*
- *GitHub actions for automated testing or deployment pipelines*
- *GitHub wiki for documentation and notes*

*Please also describe how (if) you plan test and evaluate your project's functionality. Do you plan to test manually or automatically? Any specific testing frameworks or libraries you plan to use?*

Testing Framework: Use unittest or pytest for automated testing.
Evaluation: Regularly test the functionality of each component manually and automatically. Ensure that backtested results are consistent with expectations.

## Potential Challenges and Roadblocks
*Identify any potential challenges or roadblocks you anticipate facing during the development of your project. For each challenge, propose strategies or solutions you might use to overcome them, which may include getting help from the TAs/instructor. This could include technical hurdles or learning new technologies.*

I'm currently considering whether it would be better to use a large amount of data to implement this project, or just select 10 representative stocks for prediction. Of course, the more data, the better the model accuracy and the better the outcome. I have two solutions: the ideal one is to collect a large number of stocks and store them in a database (MySQL), and the simpler one is to store the data in an Excel file.

Another point is that the more abstract the code, the more challenging the programming becomes, especially making it dynamic. Of course, I will ultimately decide based on my own capabilities.

## Additional Resources
*Include any additional resources, tutorials, or documentation that will be helpful for this project.*

In conclusion, this project aims to build a comprehensive quantitative trading platform that can serve as a valuable tool for both academic research and practical trading. By completing this project, I expect to gain a deeper understanding of financial data analysis, machine learning, and the intricacies of trading strategy development.


## Conclusion and Future Work
*Wrap up your project description with any final thoughts, expectations, or goals not covered in the sections above. Also briefly discuss potential future work, i.e., what could be done next to improve the project.*

Enhance Models: Explore more advanced machine learning models and techniques.
Expand Data Sources: Integrate additional financial data sources such as economic indicators and news sentiment.
