Processes 

Waterfall:
    
    focus on order, useful if security is extremely important, building an elevator, Requirements → Design → Implementation → Verification → Maintenance

    Problems: feedback is delayed, can lead to finding (big ) problems too late

    can be combined with other processes on smaller scale ( agile development)

Spiral: 

    improvement of waterfall with respect to its shortcomming, iterations instead of one single stream

Agile:

    focus on feedback loop, plan, implement, verify component after component and valuing stakeholders (putting the teams at the center)


    XP ( extreme programming):

        start small , deliver , grow software further, component after component, communication is key

    TDD:
        
        write tests before implementing

    SCRUM:

        planning backlog (define product backlog)

        Sprint( executing on backlog)

        Ceremony ( reflection about sprint and logs)



Thoughts for the lab:

The project can be broken down into main components: User infrastructure ( login, accounts, inviting to game, chatting, viewing profiles,stats) and the game itself (setting up game, executing game closing game)

witin each component we should first implement backend , then the api , and then the frontend, in each subcomponent implementing agile process

so each project component consists of a backend and a frontend component (one might be empty), each component (either backedn or frontend) has at least 1 testfile and the implementation and a readme wchih explains the component structure and functionality (especially if it consists of subcomponents)

The project components are build from the user stories and requirements