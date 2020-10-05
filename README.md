# yearn ROI Calculator Webapp

## Start in Dev Mode
```bash
docker-compose -f docker-compose.yaml -f dev-database.yaml up
```

## Roadmap
* Caching: The model is only updated every 24h. It it not necessary to let every request go directly against the database
