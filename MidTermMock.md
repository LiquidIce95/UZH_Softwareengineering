1. When evaluating whether or not a user story is goood, which is the correct appraoch and what does their initials stand for?

I: independant, meaning a user stories can be mostly be worked on without interfeering or needing other stories
N: negotiable, the story should be somewhat modifiable and not absolutely rigid.
V: valuable, the story must be significant and relevant for the user (duh)
E: estimable, the cost/effort of implementing it should be roughly known
S: small, specially in SCRUM it should be completet within a sprint 
T: testable,


2. What is the ideal order of capturing requirements such that the team can start with creating and assigning tasks?
elicitaion: User expresses his needs in the roal,goal ,benefit format
analysis: User stories are evaluated based on INVEST
reification: contradictions and inaccuracies are dealt with with user themselv
validation: last version is verfied by user

then to the stories Done, Time estimate and priority are added

3. What is the difference between a connector and a interface? Provide an examaple
connector is the medium of communication, interface is the contract of communition ( or formalization)
function signature is interface, function call is the connector

4. Why are interfaces even needed? Name 3 reasons
  1. Abstraction of the module via information hiding (allows use with minimal knowledge of module)
  2. possibility of refactoring the module 
  3. reduces complexity by having only one clear accesspoint of module 

5. what are drawbacks of interfaces, name 2
  1. Inteface itself must be stable, changes in interface my lead to code crashes on Users Projects.
  2. Designing good interfaces is difficult since the interface mask should be completely defined almost upfront and cannot be changed later

6. What are the basic method names for REST apis
  1.POST,PUT,DELETE,GET

7. Give two different examples endpoint which does not strictly adhere to REST specification
  1.PUT /updateUser, and requestbody has parameters, better is:
  PUT /Users/{UserId} where UserId is the user to be udpated 

  2. POST /users/{userId} this endpoint returns the user with given id wich is wrong since POST should be used for creating ressources

8. What is the definition of architecture?
  organization of code

9. considering modules, what should maximized and minimazed ? why do we even bother?
  maximize cohesion within module and minimize coupling between modules, to minimize complexity of architecture counted by number of lines 

10. what is the difference between encaplulation and information hiding?
  encapsulation is usually used in the context of specific languages, and refers to features such as classes, functions where
  the scope of code can be limited, it encapsulates by making the implemetation inaccessable to outside scope.

  information hiding: is a abstract concept and refers to mathematical abstraction itself, meaning that a subset of information of something is 
  ignored

11. what is the advantage of favouring immutability?
  The user cannot change the internal representation of object and thus assumptions made (CONTRACTS) of other parts of the API are not broken, not leading to api errors. leaving objects mutable would give the user more usability but its much more difficult to work with that representation since Users might completely change it 

12. you are tasked with developing an api for a car where the api provides functionality to use a car via code. provide one example of bad api design which break the principle of "do one thing"

  api.engineStartAndStop(boolean: b), should be changed to 
  api.engineStart(), api.engineStop()

13. using the same context as 12, provide an example of an improvement of the principle "avoid long parameter list"
  api.modifyEngine(float:capacity,float:combustion,string:model)
  api.modifyEngine(Engine: engine) where Engine is a object which has the necessary attributes and the endpoint checks for those which are not the default value or null and overwrites those 

13. using the same context as 12, provide an example of an improvement of the principle "avoid exceptional returns"

  api.getEngine() returns null if no engine is in vehicel
  should return an Engine object with all default values where it can be inferred that no engine must be present

