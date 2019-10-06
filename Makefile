
clean:
	rm -rf node_modules/
	rm -rf packages/client/node_modules/
	rm -rf packages/server/node_modules/

init:
	yarn

build:
	yarn workspace client run build
	yarn workspace server run build