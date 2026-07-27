importScripts('https://www.gstatic.com/firebasejs/10.7.1/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.7.1/firebase-messaging-compat.js');

firebase.initializeApp({
  apiKey: "AIzaSyCOKKBSbZJk8QSGvj1CPYQb_kjQb1tXO6s",
  authDomain: "starlet-registor.firebaseapp.com",
  projectId: "starlet-registor",
  storageBucket: "starlet-registor.firebasestorage.app",
  messagingSenderId: "904193225045",
  appId: "1:904193225045:web:0c9ed3f3d7251862ff7fdc"
});

const messaging = firebase.messaging();

messaging.onBackgroundMessage(function(payload) {
  const notificationTitle = payload.notification.title;
  const notificationOptions = {
    body: payload.notification.body,
    icon: '/channels4_profile.jpg',
    badge: '/channels4_profile.jpg'
  };
  self.registration.showNotification(notificationTitle, notificationOptions);
});