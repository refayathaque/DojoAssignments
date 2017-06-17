export class User {
    constructor(
    public name: string = "",
    public email: string = "",
    public password: string = "",
    public created_at: Date = new Date(),
    public updated_at: Date = new Date()
  ){}
}

// 'Public' because it needs to be exported?
// MUST IMPORT IN TO COMPONENT.TS!
