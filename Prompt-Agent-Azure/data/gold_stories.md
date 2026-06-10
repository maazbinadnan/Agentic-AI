Scenario: System successfully generates recommendations based on user tags
  Given the student is logged into the platform
  And the student has selected the interest tags "Data Analytics" and "Soccer"
  When the student navigates to the "Discover" dashboard
  Then the system should display a "Recommended for You" section
  And the list should include societies matching at least one of the selected tags
  And the list should be sorted by the highest number of matching tags

Scenario: No matching societies found for selected tags
  Given the student has selected interest tags that do not match any active societies
  When the student navigates to the "Discover" dashboard
  Then the "Recommended for You" section should display the message "We couldn't find exact matches, but here are some popular societies!"
  And the system should display the top 3 most popular societies overall

Scenario: Successfully sending targeted event notifications
  Given the society executive is on the "Create Event" page
  And the executive has filled in all required event details
  And the executive has applied the tag "Artificial Intelligence" to the event
  When the executive clicks "Publish Event"
  Then the system should save the event to the database
  And an automated push notification should be queued for all students who have the "Artificial Intelligence" tag in their profile

Scenario: Publishing an event without tags
  Given the society executive is on the "Create Event" page
  When the executive attempts to click "Publish Event" without adding any tags
  Then the system should prevent the publication
  And the system should display a validation error stating "Please select at least one interest tag to publish this event."


Scenario: Student attempts to RSVP to a conflicting event
  Given the student has synced their personal calendar with the platform
  And the student has a calendar block titled "Shift" from 18:00 to 20:00 on Friday
  When the student attempts to RSVP to an event scheduled for 19:00 on Friday
  Then the RSVP button should be disabled
  And the system should display a warning message stating "This event conflicts with an existing item on your calendar."