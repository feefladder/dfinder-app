import { createStore} from 'vuex'

export interface cycle {
  description: string,
  diagrams: string[],
  verbal: string[],
  start: number,
}

export interface ref {
  description: string,
  diagrams: string[],
  verbal: string[],
  division: number,
  cycle: cycle,
}

export interface refs {
  total: number,
  Instructions: ref[],
}

// const API_BASE = "http://127.0.0.1:5000/"
const port = location.port;
const host = location.hostname;
const API_BASE = `${location.protocol}//${host}:${port}/api/`
const API_FUNCTION_CALC_DIVISIONS = API_BASE + 'calc-divs-svg/'
const API_FUNCTION_FOLD_CYCLE = API_BASE + 'fold-cycle-svg/'

export default createStore<refs>({
  state: {
    total: 0,
    Instructions: []
  },
  mutations: {
    SET_INSTRUCTIONS(state: refs, instructions: ref[]) : void {
      state.Instructions = instructions;
      const regex = /for: ([0-9]*)\//;
      for (const i in state.Instructions) {
        const div = regex.exec(state.Instructions[i].description)
        if (div){ //this is always true, but Typescript was complaining
          state.Instructions[i].division = +div[1];
        }
      }
    },
    SET_TOTAL(state: refs, total: number) : void {
      state.total = total;
    },
    ADD_CYCLE(state: refs, cycle: cycle) : void {
      const instruction = state.Instructions.find((ref) => ref.division == cycle.start);
      if (instruction){
        instruction.cycle = cycle;
      }
    },
  },
  actions: {
    calcDivisions({commit}, nDivisions: number){
      fetch(`${API_FUNCTION_CALC_DIVISIONS}${nDivisions}`)
        .then((result) => result.json() )
        .then((instructions) => {
          commit("SET_INSTRUCTIONS", instructions.Instructions);
        })
      commit("SET_TOTAL", nDivisions);
    },
    foldCycle({commit}, start: number){
      fetch(`${API_FUNCTION_FOLD_CYCLE}${this.state.total}/${start}`)
        .then((result) => result.json())
        .then((instruction) => {
          instruction.start = start;
          commit("ADD_CYCLE", instruction)
        });
    }
  },
  modules: {
  }
})
