# SPC-Conv-Forecast

## Current Version: 0.1

### Functionality includes:
  * Pulling most recent [Day 1 convective outlook](http://www.spc.noaa.gov/products/outlook/) from SPC
    * Saving text file in json format:
      * Currently fixing bug where coordinates are in unordered format
  * Finds most recent json file in data folder and determines whether a set of coordinates is in any event/probability combination
    * Bug where discontinuation in json coordinates (see above) leads to false outcomes
  * Shell script that determines time and whether or not a new forecast has been released
    * Very basic shell script, not much functionality
    
### Future Functionality Goals:
  * Fixing above bugs
  * Extend to Day 2, Day 3, Days 4-8 convective outlooks
  * Return event & maximum probability for a set of coordinates
