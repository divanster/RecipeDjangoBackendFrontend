import React from 'react';
// import './Profile.css'; // Assuming you have a CSS file for styling

const Profile: React.FC = () => {
    return (
        <div className="profile">
            <img src="/default_images/profile_picture.png" alt="Profile" className="img-fluid rounded-circle" />
            <h3>Your Name</h3>
            <ul>
                <li>Friends</li>
                <li>Pages</li>
                {/* Add more items as needed */}
            </ul>
        </div>
    );
};

export default Profile;
