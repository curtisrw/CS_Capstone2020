1. "use postgres"
2. "use gitlab"

This can be mobile/web/a win32/linux app, anything

Justify the database interaction

We need data generation, somehow, in any lang

Goals: "replace thermostat on wall, with something more capable/functional"

"something more like a tablet, like an ipad size"

"have main screen be always up; left 3/4ths should be floor plan"

"different indicators in each room for all sensors"

"check state of lights, doors in all rooms"

"check state of faucets, on/off"

"3 bedroom, kitchen, etc"

"must have all these components"

"right hand size screen, last quarter: temperature info, exterior, interior, what is interior set to and allow it to change"

"HVAC is continuous; no option for heatmode/coolmode/off, always maintains
temperature within 2deg as specified by user"

"Second screen! Allow navigation to screen 2 from screen one, and return to screen 1."

"screen 2 should show historical usage, cost in a multi-line graph"

"show power usage, water usage, total cost"  we could split into
power/water/cost/cost/total cost

"in usdollars"

"x axis is just numbers; don't bother with units"

"y axis is time" so basically it's fake

"say, each line is marked with its units, not the axes"

"include a legend somehow or other"

"make sure it's sensible to users"

"makes for easily graphing all 3 values on one graph"

"keep 6 months of data, and make graph scalable"

"for example, jan thru may, you might capture data from june, and this drops all of Jan off the charting"

"the entire last month falls off, at the beginning of the next month"

"6 months, 4 weeks, 1 week scalings available"

"as a webpage, check out javascript lib for graphing, it does this"

"6 month data should be up to present day, always"

"use present day data, average of week/mo/6mo to calculate expected costs i.e. prediction for coming weeks in a month"

"math minor: maybe check out your own cool formula"

"show current total and predicted total side by side"

"Prediction/current total are not changed by graph scaling"

"Admin page option, or utility page separately"

"Such page allows for remote changing of state: change state of lights, doors, sensors, faucets"

"it's unrealistic for the real world, but do it in the demo"

"and have this make the system react to these changes"

"just a list of valid sensors"

"more for the main page: optionally make it to where the sensors are possible to turn on/off on main screen, like for lights specifically; make it sensible"

"that's it"
