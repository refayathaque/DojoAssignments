export class User {
    constructor (
    public firstname: string = "",
    public lastname: string = "",
    public birthdate: Date,
    public username: string = "",
    public email: string = "",
    public password: string = "",
    public confirmpassword: string = "",
    public created_at: Date = new Date(),
    public updated_at: Date = new Date()
    ) {}
}
