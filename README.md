# Caldera
Rapid generation of sample temporal data for load testing.

## Commands
All commands assume date / times are specified in ISO 8601 format.

### Erupt
Generate a specific number of points repeatedly on a certain interval in seconds. This command will continually generate
 random spatially distributed points on the given interval until interrupted. These points will be distributed in time
 between the present time less the interval and the present time.
 
```
python manage.py erupt count interval
```

### Vent
Generate a specific number of points between a start and end time. This command will randomly distribute points across
 the globe, as well as, randomly between the start and end time.

```
python manage.py vent count start end
```