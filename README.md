# yearn Vault ROI Calculator Webapp

## Start in Dev Mode
```bash
docker-compose -f docker-compose.yaml -f dev-database.yaml up
```

## Roadmap
* Caching: The model is only updated every 24h. It it not necessary to let every request go directly against the database
* Add a drop down to “Horizon” for a custom date/range.
* Add additional "%-gain" metrics for a direct ROI number. Either to the chart or as separate table.
* Add a "hypothetical value of <configurable> <asset>" functionality like [here](https://investor.vanguard.com/mutual-funds/profile/VTSAX)
