# How to use the workflow api

Within this short documentation we want to show how to use the gitlab issue
board as an agile board for sprint planning etc.

## Prerequesities

To get the most out of this overview, you should be a bit familiar with the Agile
or Scrum workflow. The following concepts should be at least heard of:
- Sprint
- User Story
- Tasks
- Assignee

## Overview

The figure below shows the overview of the used agile board within this project.
You can find it under **Issues --> Boards**. There you can change between different
boards. In our chase we use one board for every sprint. In addition we compare a
sprint to the gitlab feature **MILESTONE**, so each **User Story** and **Task** challenged
within one **sprint** is labeled with a **MILESTONE**. This **MILESTONE** is dated with the
end of the **sprint** and is achieved with the end of the related **sprint**.

![Overview Issue Board](/docu/pictures/agile_board.JPG)

## Explanation of each list and label

To dive deaper into the usage of such an agile board, we now explain the usage of
every list in the board. On the left side, you first see the **Story** list. This list
contains every **user story** tackled within this sprint. It contains all realted taskst
to achieve the **user story**. These are so called related issues in gitlab.

![Related Issues](/docu/pictures/related_issues.JPG)

Here we focus on discussions related to the user story.

The second board list is the **to Do** list. This list contains all tasks, needed
to complete to achieve the **user story**. This means that every task related to
the user story is in this list. It should be as small featured as possible and we
additionally estimate a time it takes to complete this task (Remember this is done
within the sprint planning and as a team). After listing every task we need to tackle
and the sprint itself begins, we can start working on the tasks.

Everyone who decides to start working on a task, assignes theirselve and moves the
issue from the **to Do** board to the **Doing** board, indicating that he or she is
actually working on the issue.
This process does **NOT** mean that only one person can work on that task over the time.
It is best, that only one person works at it at a specific time, but after completing
a certain work, anotherone can also work on this issue. (For example. one only has 2h
to spend on that during the day, another one can continue work after the 2h of his working
mate)
Please also indicate your time spend on the specific task with the gitlab command
/spend 10 m (for example).

After you completed your task and everything is ready to review, you can open a
**Merge Request** and you can move
your card over to the **In Test** list. There you please assigne someone else and
mention him with @username in the comments.
Then, the review process starts and everything should be tested. This is done and
documented within the MR. There, required changes are listed and a few approvals
needs to check the code quality etc. After this process is done and everything works
fine, the MR can be merged and the task is finally defined as done! This means that
now is the time where you can **close** the issue.

Thats a first quick overview. Maybe we go further in depth how to use MR and how to
to a review and approvals.
