export interface Item { nombre: string; descripcion?: string; precio?: number; foto?: string; opciones?: string[]; grupo?: string; destacado?: boolean; pose?: string }
export interface Categoria { id: string; nombre: string; lado: string; items: Item[] }
export interface Carta { actualizada: string; categorias: Categoria[] }

export interface Tostador { id: string; nombre: string; color: string; tinta: 'carbon' | 'crema'; holo?: boolean }
export interface Cafe {
  id: string; tostador: string; nombre: string;
  origen?: string; proceso?: string; variedad?: string; notas?: string[]; mood?: string;
  en_barra: boolean; pose?: string;
}
export interface Cafes { tostadores: Tostador[]; cafes: Cafe[] }

export interface Evento {
  id: string; titulo: string; fecha: string; desde?: string; hasta?: string;
  descripcion?: string; flyer?: string; reserva?: string;
}

export interface Horario { dias: string; semana?: number[]; turnos: string[] } // semana: 0 = domingo … 6 = sábado
export interface Local {
  nombre: string; direccion: string; ciudad: string; horarios: Horario[];
  whatsapp: string; instagram: string; maps: string; mapsEmbed?: string; lema?: string; nominacion?: string;
}
