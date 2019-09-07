# Angular

- client-side JS framework
- single page, reactive web apps

```zsh
ng new react-app
ng serve
ng generate component servers
ng g c servers --skipTests
```

## Binding

```jsx
// property binding
<app-persons [personList]="persons"></app-persons>
// event binding
<button (click)="onCreatePerson()">Create</button>
// string interpolation
<li *ngFor="let person of personList">{{ person }}</li>
// two-way binding
<input type="text" id="name" [(ngModel)]="enteredName">
```

## Data passing

```jsx
<app-persons [personList]="persons"></app-persons>
...
@Component({...})
export class PersonsComponent {
  @Input() personList: string[];
}
```

## ngIf else

```jsx
<p *ngIf="serverCreated; else noServer">Server '{{ serverName }}' was created</p>
<ng-template #noServer><p>No server created</p></ng-template>
```

## Emitting Data

```jsx
<input type="text" id="name" [(ngModel)]="enteredPersonName">
<button (click)="onCreatePerson()">Create</button>
```

```jsx
import { Component, Output, EventEmitter } from '@angular/core';

@Component({...})
export class PersonInputComponent {
  @Output() personCreate = new EventEmitter<string>();
  enteredPersonName = '';

  onCreatePerson() {
    console.log('Created a person: ' + this.enteredPersonName);
    this.personCreate.emit(this.enteredPersonName);
    this.enteredPersonName = '';
  }
}
```

```jsx
<app-person-input (personCreate)="onPersonCreated($event)"></app-person-input>
```

```jsx
export class AppComponent {
  persons: string[] = ['Max', 'Manuel', 'Anna'];
  onPersonCreated(name: string) {
    this.persons.push(name);
  }
}
```

## Routing

```jsx
const routes: Routes = [
  { path: '', component: PersonsComponent },
  { path: 'input', component: PersonInputComponent },
];

// app component
<a routerLink="/">Person List</a> | <a routerLink="/input">Input</a>
<router-outlet></router-outlet>

```

## Services

- services can be injected into other components

```jsx
import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class NameService {
  persons: string[] = ['Max', 'Manuel', 'Anna'];
  addPerson(name: string) {
    this.persons.push(name);
  }
}
```

```jsx
import { Component, OnInit } from '@angular/core';
import { PersonsService } from './persons.service';

@Component({...})
export class PersonsComponent implements OnInit {
  personList: string[];
  constructor(private personsService: PersonsService) {}
  ngOnInit() {
    this.personList = this.personsService.persons;
  }
}
```

## Updating an array on change

```jsx
import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class PersonsService {
  personsChanged = new Subject<string[]>();
  public persons: string[] = ['Max', 'Manuel', 'Anna'];

  addPerson(name: string) {
    this.persons.push(name);
    this.personsChanged.next(this.persons);
  }
}
```

```jsx
import { Component, OnInit, OnDestroy } from '@angular/core';
import { PersonsService } from './persons.service';
import { Subscription } from 'rxjs';

@Component({...})
export class PersonsComponent implements OnInit, OnDestroy {
  personList: string[];
  private personListSubs: Subscription;

  constructor(private personsService: PersonsService) {}
  ngOnInit() {
    this.personList = this.personsService.persons;
    this.personListSubs = this.personsService.personsChanged.subscribe(
      persons => (this.personList = persons)
    );
  }
  onRemovePerson(personName: string) {
    this.personsService.removePerson(personName);
  }
  ngOnDestroy() {
    this.personListSubs.unsubscribe();
  }
}
```

## HTTP Requests

`persons.service.ts`

```jsx
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Subject } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({ providedIn: 'root' })
export class PersonsService {
  personsChanged = new Subject<string[]>();
  persons: string[];

  constructor(private http: HttpClient) {}

  fetchPersons() {
    this.http
      .get<any>('https://swapi.co/api/people')
      .pipe(
        map(response => {
          return response.results.map(item => item.name);
        })
      )
      .subscribe(data => {
        this.personsChanged.next(data);
      });
  }

  addPerson(name: string) {
    this.persons.push(name);
    this.personsChanged.next(this.persons);
  }
}
```

`persons.component.ts`

```jsx
import { Component, OnInit, OnDestroy } from '@angular/core';
import { PersonsService } from './persons.service';
import { Subscription } from 'rxjs';

@Component({...})
export class PersonsComponent implements OnInit, OnDestroy {
  personList: string[];
  private personListSubs: Subscription;

  constructor(private personsService: PersonsService) {}
  ngOnInit() {
    this.personListSubs = this.personsService.personsChanged.subscribe(
      persons => (this.personList = persons)
    );
    this.personsService.fetchPersons();
  }
  onAddPerson(personName: string) {
    this.personsService.addPerson(personName);
  }
  ngOnDestroy() {
    this.personListSubs.unsubscribe();
  }
}

```

## Loading Screen

```jsx
<p *ngIf="isFetching">Loading...</p>
<ul *ngIf="!isFetching">
  <li *ngFor="let person of personList" (click)="onRemovePerson(person)">{{ person }}</li>
</ul>
```
