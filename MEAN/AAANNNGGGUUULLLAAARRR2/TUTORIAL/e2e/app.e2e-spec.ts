import { TUTORIALPage } from './app.po';

describe('tutorial App', () => {
  let page: TUTORIALPage;

  beforeEach(() => {
    page = new TUTORIALPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
