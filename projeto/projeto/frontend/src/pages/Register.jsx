import React, { useState, useEffect } from 'react';
import '../css/Register.css';
import '../css/NavBar.css';
import { useNavigate } from "react-router-dom";

function RegisterForm() {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [birthDate, setBirthDate] = useState('');
  const [gender, setGender] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [agreeTerms, setAgreeTerms] = useState(false);
  const [error, setError] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    if (token) {
      navigate('/');
      window.location.reload();
    }
  }, [navigate]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');
    setSuccessMessage('');

    if (!firstName.trim() || !lastName.trim() || !birthDate || !gender || !email.trim() || !password || !confirmPassword) {
      setError('All fields are required.');
      return;
    }

    if (!['M', 'F'].includes(gender)) {
      setError('Gender must be M or F.');
      return;
    }

    if (!/\S+@\S+\.\S+/.test(email)) {
      setError('Invalid email format.');
      return;
    }

    if (password.length < 6) {
      setError('Password must be at least 6 characters long.');
      return;
    }

    if (password !== confirmPassword) {
      setError('Passwords do not match.');
      return;
    }

    if (!agreeTerms) {
      setError('You must agree to the terms and conditions.');
      return;
    }

    const payload = {
      grupo_nome: "Meu Grupo",
      nome_primeiro: firstName,
      nome_ultimo: lastName,
      data_nasc: birthDate,
      genero: gender,
      numero_cc: 0,
      estado_civilid_estado_civil: 1,
      nacionalidadeid_nacionalidade: 1,
      password,
      email
    };

    try {
      const response = await fetch('http://localhost:8000/utilizador/create_first/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload)
      });

      const data = await response.json();

      if (response.ok) {
        setSuccessMessage("Conta criada com sucesso! Redirecionando...");
        setFirstName('');
        setLastName('');
        setBirthDate('');
        setGender('');
        setEmail('');
        setPassword('');
        setConfirmPassword('');
        setAgreeTerms(false);

        setTimeout(() => {
          navigate('/login');
        }, 2000); // Redireciona após 2 segundos
      } else {
        setError(data.error || 'Registration failed.');
      }
    } catch (error) {
      setError('Network error. Please try again.');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="register-form">
      <h2>Register</h2>
      {error && <p className="error-message">{error}</p>}
      {successMessage && <p className="success-message">{successMessage}</p>}

      <div className="form-group">
        <label htmlFor="firstName">First Name:</label>
        <input
          type="text"
          id="firstName"
          className="form-control"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="lastName">Last Name:</label>
        <input
          type="text"
          id="lastName"
          className="form-control"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="birthDate">Date of Birth:</label>
        <input
          type="date"
          id="birthDate"
          className="form-control"
          value={birthDate}
          onChange={(e) => setBirthDate(e.target.value)}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="gender">Gender (M/F):</label>
        <select
          id="gender"
          className="form-control"
          value={gender}
          onChange={(e) => setGender(e.target.value)}
          required
        >
          <option value="">Select</option>
          <option value="M">Male (M)</option>
          <option value="F">Female (F)</option>
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          className="form-control"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          className="form-control"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="confirmPassword">Confirm Password:</label>
        <input
          type="password"
          id="confirmPassword"
          className="form-control"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          required
        />
      </div>

      <div className="form-group">
        <input
          type="checkbox"
          id="agreeTerms"
          className="form-checkbox"
          checked={agreeTerms}
          onChange={(e) => setAgreeTerms(e.target.checked)}
          required
        />
        <label htmlFor="agreeTerms" className="form-label-checkbox">
          I agree to the <a href="/terms" target="_blank" rel="noopener noreferrer">Terms and Conditions</a>
        </label>
      </div>

      <button type="submit" className="register-button">Register Now</button>
      <p className="login-link">
        Already have an account? <a href="/login">Log in</a>
      </p>
    </form>
  );
}

export default RegisterForm;
