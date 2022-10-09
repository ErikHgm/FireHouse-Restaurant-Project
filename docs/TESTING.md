Return to [README.md](/README.md)  

# Testing  

## Methodology  
Testing was done throughout the process while developing the project by the use of Django debug pages and printing statements to check that the code functioned accordingly. In addition, thorough testing has been performed and is described below, it contains of manual test to check that all user stories and acceptance criteria are met, as well as testing and validating the code with different online tools as presented below.  

&nbsp;

### Test Cases  
&nbsp;
### User Stories

#### Menu page
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Customer can view menu page | Test menu link and child links within the menu page | Being able to open and browse the menu without errors | PASS |

#### Registration
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Customer signup page | Test link is working | Customer is directed to the signup page | PASS |
| Customer signup - Form validation | Submit empty form | Form validation prompts the user | PASS |
| Customer signup - Form validation | Submit invalid email address | Form validation prompts the user | PASS |
| Customer signup - Form validation | Submit invalid password | Form validation prompts the user | PASS |
| Customer signup - Form validation | Submit non matching passwords | Form validation prompts the user | PASS |
| Customer signup - Form validation | Submit already taken username | Form validation prompts the user | PASS |
| Customer login page | Test link is working | Customer is directed to the login page | PASS |
| Customer login - Form validation | Submit incorrect password | Form validation prompts the user | PASS |
| Customer login - Form validation | Submit incorrect name | Form validation prompts the user | PASS |
| Customer login - Form validation | Submit incorrect name | Form validation prompts the user | PASS |
| Customer Logout page | Test link is working | User is logged out | PASS |

#### Bookings 
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Form validation Booking page | Check that each required field is working correctly in the form | Form validation prompts the user | PASS |
| Submit button Booking page | Click the submit button to check that the booking is saved | Sucess message and redirect to mybooking page | PASS |
| Bookings are shown on mybookings page | Check that each booking for a user are shown on the mybookings page | Individual cards of each booking is shown with the corresponding booking details | PASS |
| Bookings can be edited | Check that the edit button works and that the updated booking is submitted to the mybooking page when edited | Booking is updated with the corresponding booking details | PASS |
| Bookings can can be deleted | Check that the delete button works and that the deleted booking is removed from the mybooking page when deleted | Mybooking list is updated | PASS |

#### Navbar
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Navbar | Check that each link is working correctly | Customer is able to open each link to browse the webpage for information about the restaurant | PASS |

#### Admin
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Admin login - Form validation | Submit incorrect password | Form validation prompts the user | PASS |
| Admin login - Form validation | Submit incorrect name | Form validation prompts the user | PASS |
| Admin login - Form validation | Submit incorrect name | Form validation prompts the user | PASS |
| Admin panel | Owner is able to update bookings | Booking is updated with the corresponding booking details | PASS |
| Admin panel | Owner is able to delete bookings | Booking is deleted from current booking list | PASS |


## Further Testing
-   The website was thoroughly tested on different browsers including Google Chrome, Internet Explorer, Safar and Microsoft Edge. Extensive testing was performed to make sure all the links and navigation work properly. Testing on different devices to make sure it scales properly using the below tools:  
    -   [Responsivetesttool](http://responsivetesttool.com/)
    -   [Google Devtools](https://developer.chrome.com/docs/devtools/open/)  
  

-   [W3C Markup Validator](https://validator.w3.org/nu/) 
    - No errors or warnings that are relevant was shown 

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) 
    - No errors or warnings that are relevant was shown 

-   [Python Validator](https://extendsclass.com/python-tester.html#:~:text=To%20check%20your%20code%2C%20you,use%20this%20python%20checker%20tool.) 
    - No errors or warnings that are relevant was shown 



Return to [README.md](/README.md)