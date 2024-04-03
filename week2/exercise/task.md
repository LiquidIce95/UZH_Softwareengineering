1.
develop the following program using following assumptions:

1) during development, no changes in requirements can occure, since the law prescribes how the software has to look like and what functionalities it has,

2) during development, requirements are garuanteed to change constantly, especially additional requirements can rise "out of thin air"

programm:
As a User I want to register my account in a database to save my profile settings
As a User I want to be able to login and change my profile settings to update information about myself

wich appraoch should process should be used?
  for 1 waterfall, for 2 spiral or agile 

How does the selection of the procsess influence the actual activity of coding the programm?
  in waterfall, after design the entire app can be coded and then tested. The app entire app could be coded in one go without getting customer feedback since the requirements are fixed and no changes expected. After that the maintenance is more about upholding the requirements rather than making changes.


  with spiral or agile a first basic prototype with maybe one feature is implemented and tested, then the requirements are updated and the next
  feature is implemented and tested so the app should be strucutred in modules which can be implemented one after another and which make up the entire application.

2.
Both SCRUm and XP follow the agile manifesto

1) how do both adhere to the agile manifesto?
  SCRUM uses self-organizing teams which satisfies the collaboration principle, SCRUM uses small evelopment cycles called sprints whihc satisfies
  the incremental progress principle.
  XP uses pair programming to satisfy the collaboration principle and collective code ownership. They also make small builds which satisfies the incremental progress principle.
2) how do both differ?
  XP uses pair programming and TDD, SCRUM does not necessarily use those

3) elaborate how SPRINTS are executed in SCRUM
  first the product backlog is created, then foreach sprint: the sprint backlog is created consisting of User stories and tasks, daily meetings with scrum mster define who is responsible for whihc task, tasks are designed to be completed within a day so progress is easy to measure. Burncharts are used to track that progress. After a sprint requirements are re-evaluated.

4) what are potential pitfalls of SCRUM?
  Once a sprint is started usually the requirements are fixed, if customer make changes its up to the scrum master to decided whether or not to inform the team, on the one hand the change may make the sprint redundant or unnecassary on the other it could disturb the flow of the team. Obviously if the daily meetings are not kept to a absolute minimal length, they can consume a lot of time. Finally Sprints , as the name implies can be taxing for the teams if the workload is too high.

5) Create a scenario where SCRUM is unsuitable but XP is 
  A project with very high complexity, like running a scientific simulation (physics simulation) where the data could have real world negative implications. 
  Maybe software which simulates bacteria reacting to certain treatment. Pair programming could help catch errors or bad design very early on. In addition the close customer collaboration makes sure that the requirements are constantly updated. Since XP also emphasises sustainability of the project progress its less prone to errors albeit a bit slower ( SCRUM uses literally something thats called burndown chart...) Also TDD further emphasizes security since the tests can be created beforehand with the biologists which will be using the simulation. Especially the biologists may have facts that the simulation must correctly fullfill in order to be accurate.

6) finally, create a scenario where SCRUm is suitable but XP not
  a simple project where the features are not complex and not security sensistive like in most webbapps or games.
  Pair programming would rather impede progress since the tasks are so easy tath both programmers are more than capable of doing it themselves, (whereas in the medicale example both would be rather helpless because of the specific knowledge needed). also TDD is not as beneficial since the customers are not knowledgable enough to express requirements in form of specific tests. Sprints are therefore also more managable because of the more simple nature of the project.
