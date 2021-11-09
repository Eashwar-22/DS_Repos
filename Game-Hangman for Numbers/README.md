---
## Hangman for numbers - Only using if & for loops
---
**Objective :**

- Identify the number by guessing possible digits to fill in the blanks.
- You get a hint before the final chance.
- You get penalized for guessing the wrong digit or an already used digit, maximum of 2 mistakes can be made.
- There is no entry limit.
- Possible hints:
    * If only one digit is left to be guessed, hint at whether the digit is odd or even.
    * If more than one digit is left to be guessed (with duplicates), hint at the sum of the remaining digits.
    * Note : Hint can appear only once.

---

**Gameplay**

<img width="515" alt="Screenshot 2021-11-09 at 3 48 50 PM" src="https://user-images.githubusercontent.com/86509452/140906628-6fd26e85-d674-41bb-b7c4-bc567bb9c9a1.png">
<img width="510" alt="Screenshot 2021-11-09 at 3 49 20 PM" src="https://user-images.githubusercontent.com/86509452/140906642-5de37a32-3c82-4d84-ad04-b837e04168eb.png">
<img width="503" alt="Screenshot 2021-11-09 at 3 49 46 PM" src="https://user-images.githubusercontent.com/86509452/140906648-db4f6482-502c-4be2-8f94-1da8a2e533f1.png">

---

**Sample information stored for one game session**

<img width="727" alt="Screenshot 2021-11-09 at 3 53 11 PM" src="https://user-images.githubusercontent.com/86509452/140907043-f88583a9-196c-4753-bc18-1f9677839d47.png">

---


**Update**

- Store the gameplay information for each session per user.
- The data could be used to understand the activity performed after each turn based on the game status.
- The current version of the code already stores the information in the Database folder, there is more potential to the information that the game can offer.
---
**Potential**

- Store more information on gameplay.
- Bring GUI into the game and implement the same on pygame.
