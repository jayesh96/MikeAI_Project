Problem Statements as mentioned in mail:
The task would include building a Django application coupled with a minimal ReactJS/Angular JS User Interface.

CRUX: Unit element is a "Case" and each case has some properties like:
1. Case Title (Eg. Facebook Vs. Tesla)
2. Case ID (Unique Identifier)
3. Mentioned in (Cases where self-case has been mentioned)
4. Mentions (Cases that are mentioned in self-case)
5. Body (Text)
6. Date of Judgement (Date)

First, you would need to use some Fake data using Faker (or whatever you feel like using) to populate your Models. (see the crux above to get good understanding of what Fake data would look like)
About 50 Fake Cases would be a good number to go.

Second, on UI part, the Component would be a Graph that plots the cases as in the picture below:
<A graph image here>

Here, cases are plotted according to their respective Years (Year component of Date of Judgement)

X-Axis: Year
Y-Axis: Can plot it randomly (or by the Month Component too)
Radius of Circle: More the count of "Mentions" in self-case, greater is the radius

On hovering over each Circle i.e. Case, the relation of "Mentioned in" can be visualized by an OUTWARDS ARROW as shown in the picture below.

TASK TIMELINE
Day 1: Set up Django Framework for the project and added models.py
Day 2:Get the insights about HighCharts.js, D3.js and selected D3.js for the graph plotting 

TASK PENDING:
1)UI needs to be updated
2) Mentions field is dummy
3) Add Scattered Bubble and directed graph in the same graph



