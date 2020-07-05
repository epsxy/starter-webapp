import { browser, by, element } from 'protractor';

export class AppPage {
    navigateTo(): Promise<unknown> {
        return browser.get(browser.baseUrl) as Promise<unknown>;
    }

    getHomeTitle(): Promise<string> {
        return element(by.css('app-root .root__title')).getText() as Promise<string>;
    }
}
