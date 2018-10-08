def applicant_selector(gpa,ps_score,ec_count):
  message = "This applicant should be rejected."
  if (gpa >= 3):
    if (ps_score >= 90):
      if (ec_count >= 3):
        message = "This applicant should be accepted."
      else:
      	message = "This applicant should be given an in-person interview."
  return message
