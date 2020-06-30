import { browser, by, element } from 'protractor';

export class AppPage {
    navigateTo() {
        return browser.get(browser.baseUrl) as Promise<any>;
    }

    getMainTitle() {
        return element(by.css('.root__title')).getText() as Promise<string>;
    }
}
