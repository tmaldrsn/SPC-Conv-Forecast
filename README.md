# SPC-Conv-Forecast

## Current Version: 0.2

### Functionality includes:
 * Eliminated need for JSON file handling by using arrays for each line
 * Using shapely library to plot probability boundaries
   * https://pypi.org/project/Shapely/
 * Goes to SPC website and pulls most recently available Day 1 convective outlook
 * Plotting capabilities using matplotlib library and shapely library
   * Four separate plotting scripts ==> Tornado, Hail, Wind and Categorical probabilities
   * Uses information from 2010 census to plot contiguous US boundaries
     * https://www.census.gov/geo/maps-data/data/cbf/cbf_nation.html
     
### Goals for v0.3:
  * Implement Day 2, 3, 4-8 outlooks
  * Ability to import text files from previous forecasts
  * Figure out early morning forecast schedule (0600, 1200 forecast timing)

## Previous Versions:     
     
### Version 0.1:

#### Functionality includes:
  * Pulling most recent [Day 1 convective outlook](http://www.spc.noaa.gov/products/outlook/) from SPC
    * ~~Saving text file in json format:~~
      * ~~Currently fixing bug where coordinates are in unordered format~~
  * ~~Finds most recent json file in data folder and determines whether a set of coordinates is in any event/probability combination~~
    * ~~Bug where discontinuation in json coordinates (see above) leads to false outcomes~~
  * Shell script that determines time and whether or not a new forecast has been released
    * Very basic shell script, not much functionality
