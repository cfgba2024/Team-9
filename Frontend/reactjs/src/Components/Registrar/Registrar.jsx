import React, { useState } from "react";
import "./Registrar.css";

export default function OrganizationRegistrationForm() {
    const [formData, setFormData] = useState({
        organizationName: "",
        email: "",
        password: "",
        description: ""
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Here you could add form validation or API call to register the organization
        console.log("Te has postulado con exito - Te enviaremos un mail con la confirmacion", formData);
    };

    return (
        <div className="registration-form-container">
            <h2>Queres participar?</h2>
            <form onSubmit={handleSubmit} className="registration-form">
                <div className="form-group">
                    <label htmlFor="organizationName">Nombre del colegio</label>
                    <input
                        type="text"
                        id="organizationName"
                        name="organizationName"
                        value={formData.organizationName}
                        onChange={handleChange}
                        required
                    />
                </div>
                
                <div className="form-group">
                    <label htmlFor="email">Email</label>
                    <input
                        type="email"
                        id="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="description">Notas</label>
                    <textarea
                        id="description"
                        name="description"
                        value={formData.description}
                        onChange={handleChange}
                    ></textarea>
                </div>

                <button type="submit">Postularse</button>
            </form>
        </div>
    );
}
