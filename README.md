# Caldera
Rapid generation of sample temporal data for load testing.

## Commands
### Erupt
Generate a specific number of points repeatedly on a certain interval in seconds. This command will randomly distribute
 points across the globe on the given interval starting at now - interval. These points will be distributed in time
 between the last interval and the present time.
 
```
python manage.py erupt count interval
```

### Vent
Generate a specific number of points between a start and end time. This command will randomly distribute points across
 the globe, as well as, randomly between the start and end time.

```
python manage.py vent count start end
```