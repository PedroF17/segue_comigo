import React, { useState } from 'react';
import '../css/Register.css'; // Import the CSS file
import '../css/NavBar.css';
import {Link} from "react-router-dom";

function RegisterForm() {
  const [groupName, setGroupName] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [birthDate, setBirthDate] = useState('');
  const [gender, setGender] = useState('');
  const [ccNumber, setCcNumber] = useState('');
  const [maritalStatus, setMaritalStatus] = useState('');
  const [nationality, setNationality] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [agreeTerms, setAgreeTerms] = useState(false);
  const [error, setError] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  const handleGroupNameChange = (event) => {
    setGroupName(event.target.value);
  };

  const handleFirstNameChange = (event) => {
    setFirstName(event.target.value);
  };

  const handleLastNameChange = (event) => {
    setLastName(event.target.value);
  };

  const handleBirthDateChange = (event) => {
    setBirthDate(event.target.value);
  };

  const handleGenderChange = (event) => {
    setGender(event.target.value);
  };

  const handleCcNumberChange = (event) => {
    setCcNumber(event.target.value);
  };

  const handleMaritalStatusChange = (event) => {
    setMaritalStatus(event.target.value);
  };

  const handleNationalityChange = (event) => {
    setNationality(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handleConfirmPasswordChange = (event) => {
    setConfirmPassword(event.target.value);
  };

  const handleAgreeTermsChange = (event) => {
    setAgreeTerms(event.target.checked);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');
    setSuccessMessage('');

    if (!groupName.trim()) {
      setError('Group name is required.');
      return;
    }

    if (!firstName.trim()) {
      setError('First name is required.');
      return;
    }

    if (!lastName.trim()) {
      setError('Last name is required.');
      return;
    }

    if (!birthDate) {
      setError('Date of birth is required.');
      return;
    }

    if (!gender) {
      setError('Gender is required.');
      return;
    }

    if (!ccNumber.trim()) {
      setError('Citizen Card number is required.');
      return;
    }

    if (!maritalStatus) {
      setError('Marital status is required.');
      return;
    }

    if (!nationality) {
      setError('Nationality is required.');
      return;
    }

    if (!email.trim()) {
      setError('Email is required.');
      return;
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      setError('Invalid email format.');
      return;
    }

    if (!password) {
      setError('Password is required.');
      return;
    } else if (password.length < 6) {
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

    const registrationUrl = 'http://localhost:8000/api/auth/register/'; // Replace with your actual Django registration URL

    try {
      const response = await fetch(registrationUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          group_name: groupName,
          nome_primeiro: firstName,
          nome_ultimo: lastName,
          data_nasc: birthDate,
          genero: gender,
          numero_cc: ccNumber,
          estado_civil: maritalStatus,
          nacionalidade: nationality,
          password: password,
          email: email,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        setSuccessMessage(data.message);
        // Optionally reset the form
        setGroupName('');
        setFirstName('');
        setLastName('');
        setBirthDate('');
        setGender('');
        setCcNumber('');
        setMaritalStatus('');
        setNationality('');
        setEmail('');
        setPassword('');
        setConfirmPassword('');
        setAgreeTerms(false);
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
        <label htmlFor="groupName">Group Name:</label>
        <input
          type="text"
          id="groupName"
          className="form-control"
          value={groupName}
          onChange={handleGroupNameChange}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="firstName">First Name:</label>
        <input
          type="text"
          id="firstName"
          className="form-control"
          value={firstName}
          onChange={handleFirstNameChange}
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
          onChange={handleLastNameChange}
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
          onChange={handleBirthDateChange}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="gender">Gender:</label>
        <select
          id="gender"
          className="form-control"
          value={gender}
          onChange={handleGenderChange}
          required
        >
          <option value="">Select Gender</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="ccNumber">Citizen Card Number:</label>
        <input
          type="text"
          id="ccNumber"
          className="form-control"
          value={ccNumber}
          onChange={handleCcNumberChange}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="maritalStatus">Marital Status:</label>
        <input
          type="text"
          id="maritalStatus"
          className="form-control"
          value={maritalStatus}
          onChange={handleMaritalStatusChange}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="nationality">Nationality:</label>
        <input
          type="text"
          id="nationality"
          className="form-control"
          value={nationality}
          onChange={handleNationalityChange}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          className="form-control"
          value={email}
          onChange={handleEmailChange}
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
          onChange={handlePasswordChange}
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
          onChange={handleConfirmPasswordChange}
          required
        />
      </div>

      <div className="form-group">
        <input
          type="checkbox"
          id="agreeTerms"
          className="form-checkbox"
          checked={agreeTerms}
          onChange={handleAgreeTermsChange}
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
