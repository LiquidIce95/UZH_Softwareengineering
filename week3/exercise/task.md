1. Implement the following user stories

  As X I want to print statements somewhere to Y


  As a SoftwareEngineer I want to print statements somewhere as easy as possible, to debug my code 


  As a User of the python package I want to print statements to create text onto a text file.


  this illustrates why role and goal are important


2. MOdell with UML the following User stories:

  As a User I want to create an account to save my profice settings

  As a User I want to view the profile of other people to decide whether I should text them or not

  As a User I want to be able to login with a choosen password to access the app.

  As a User I want the system to not share any information about me with third parties.


  Can you spot an inconsystency / contradiction?

  When designing the user class, all of its attributes are private since the user does not want to disclose 
  any information. But at the same time the Profile inofrmation aobut other users should be visible whihc is a contradiciton.

  Furthermore, if the user can choose its password alone, without any password requirements, someone could potentially break into the account and
  steal the data which also contradicts the last story.

2.1 without further inforamtion, try to rewrite the user stories to reach a consistent state and propose to the user.

  As a User I want to create an account to save my profile settings

  As a User I want to view the profile of other people which includes username, a profile picture and bio to decide whether I should text them or not

  As a user I want to be able to login with a choosen secure password to access the app.

  as a user I want the system to not share any information about me with third parties, apart from username, bio and profilepicture which is only shared with other users.

  As a user I can set the visibility of my profile information but username bio and picture are always visible, to be more open with users of the app only.


3. A user sends a UML diagram of the app wanted, and argues that User stories are therefore not neccesarry. What do you do?

  Since Role and goal are not captured via models  and maybe some non-functional properties and accceptance criteria I still engage with the user 
  in a conversation to capture the requirements in the user story format.


4. Considering SCRUM is used in your project. How long should a task be?
  less than 6 hours, such that it can be completed within a day, therefore when engaging with user/stakeholder large stories need to be broken down.

5. Considering XP is used in your project. What should you consider when getting requirements?
  since TDD is used, you should try to get tests from the stakeholders.

